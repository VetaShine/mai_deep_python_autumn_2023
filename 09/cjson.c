// Парсинг и сериализация json
#include <Python.h>
#include <ctype.h>

static PyObject* cjson_dumps(PyObject* self, PyObject* args) {
    // Преобразование входного словаря в строку JSON
    PyObject* input_dict;

    if (!PyArg_ParseTuple(args, "O", &input_dict)) {
        PyErr_Format(PyExc_TypeError, "Dict should be passed as argument");
        return NULL;
    }

    if (!PyDict_Check(input_dict)) {
        PyErr_Format(PyExc_TypeError, "Invalid argument. Expected dict.");
        return NULL;
    }

    PyObject* output_str = NULL;
    PyObject* items = PyDict_Items(input_dict);
    Py_ssize_t size = PyList_Size(items);
    Py_ssize_t i;

    if (!(output_str = PyUnicode_New(0, size * 2))) {
        Py_XDECREF(items);
        return NULL;
    }

    PyUnicode_AppendAndDel(&output_str, PyUnicode_FromString("{"));

    for (i = 0; i < size; i++) {
        PyObject* item = PyList_GetItem(items, i);
        PyObject* key = PyTuple_GetItem(item, 0);
        PyObject* value = PyTuple_GetItem(item, 1);

        if (!PyUnicode_CheckExact(key)) {
            PyErr_Format(PyExc_TypeError, "Invalid dictionary key. Expected string.");
            Py_DECREF(items);
            Py_DECREF(output_str);
            return NULL;
        }

        if (!PyUnicode_CheckExact(value) && !PyLong_CheckExact(value)) {
            PyErr_Format(PyExc_TypeError, "Invalid dictionary value. Expected string or number.");
            Py_DECREF(items);
            Py_DECREF(output_str);
            return NULL;
        }

        PyUnicode_AppendAndDel(&output_str, PyUnicode_FromFormat("\"%s\": ", PyUnicode_AsUTF8(key)));

        if (PyUnicode_CheckExact(value)) {
            PyUnicode_AppendAndDel(&output_str, PyUnicode_FromFormat("\"%s\"", PyUnicode_AsUTF8(value)));
        }
        else {
            PyUnicode_AppendAndDel(&output_str, PyUnicode_FromFormat("%lld", PyLong_AsLong(value)));
        }

        if (i < size - 1) {
            PyUnicode_AppendAndDel(&output_str, PyUnicode_FromString(", "));
        }
    }

    PyUnicode_AppendAndDel(&output_str, PyUnicode_FromString("}"));
    Py_DECREF(items);
    return output_str;
}


static PyObject* cjson_loads(PyObject* self, PyObject* args) {
    // Создание словаря по строке JSON
    const char* json_str;

    if (!PyArg_ParseTuple(args, "s", &json_str))
        return NULL;

    PyObject* dict = NULL;
    dict = PyDict_New();

    if (dict == NULL) {
        PyErr_Format(PyExc_RuntimeError, "Failed to create dictionary object");
        return NULL;
    }

    int pos = 0;
    PyObject* key = NULL;
    PyObject* value = NULL;
    PyObject* tmp = NULL;

    while (json_str[pos] && isspace(json_str[pos]))
        pos++;

    if (json_str[pos] == '\0') {
        Py_DECREF(dict);
        PyErr_Format(PyExc_ValueError, "JSON string is empty");
        return NULL;
    }

    if (json_str[pos] != '{') {
        Py_DECREF(dict);
        PyErr_Format(PyExc_ValueError, "JSON should start with \"{\"");
        return NULL;
    }

    pos++;

    while (json_str[pos] && json_str[pos] != '}') {
        while (json_str[pos] && isspace(json_str[pos]))
            pos++;

        if (json_str[pos] == '\0') {
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Expected key");
            return NULL;
        }

        if (json_str[pos] != '\"') {
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Key should be string beginning with \" quotation mark");
            return NULL;
        }

        pos++;
        int start = pos;

        while (json_str[pos] && json_str[pos] != '\"')
            pos++;

        if (json_str[pos] != '\"') {
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Key should be string like \"some word\"");
            return NULL;
        }

        PyObject* key_str = PyUnicode_FromStringAndSize(&json_str[start], pos - start);

        if (key_str == NULL) {
            Py_DECREF(dict);
            return NULL;
        }

        pos++;

        while (json_str[pos] && isspace(json_str[pos]))
            pos++;
        
        if (json_str[pos] == '\0') {
            Py_DECREF(key_str);
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Expected \":\" symbol and value after key");
            return NULL;
        }

        if (json_str[pos] != ':') {
            Py_DECREF(key_str);
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Expected \":\" symbol after key");
            return NULL;
        }

        pos++;

        while (json_str[pos] && isspace(json_str[pos]))
            pos++;

        if (json_str[pos] == '\"') {
            pos++;
            start = pos;

            while (json_str[pos] && json_str[pos] != '\"')
                pos++;

            if (json_str[pos] != '\"') {
                Py_DECREF(key_str);
                Py_DECREF(dict);
                PyErr_Format(PyExc_TypeError, "Value should be a number or a string like \"some value\"");
                return NULL;
            }

            value = PyUnicode_FromStringAndSize(&json_str[start], pos - start);

            if (value == NULL) {
                Py_DECREF(key_str);
                Py_DECREF(dict);
                return NULL;
            }

            pos++;
        }
        else if (isdigit(json_str[pos]) || json_str[pos] == '-') {
            start = pos;

            while (json_str[pos] && (isdigit(json_str[pos]) || json_str[pos] == '.' || json_str[pos] == '-' || json_str[pos] == '+'))
                pos++;

            tmp = PyUnicode_FromStringAndSize(&json_str[start], pos - start);

            if (tmp == NULL) {
                Py_DECREF(key_str);
                Py_DECREF(dict);
                return NULL;
            }

            value = PyFloat_FromString(tmp);
            Py_DECREF(tmp);

            if (value == NULL) {
                PyErr_Format(PyExc_ValueError, "Invalid numeric value");
                Py_DECREF(key_str);
                Py_DECREF(dict);
                return NULL;
            }
        }
        else {
            Py_DECREF(key_str);
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Expected string or numeric value");
            return NULL;
        }

        if (PyDict_SetItem(dict, key_str, value) != 0) {
            Py_DECREF(key_str);
            Py_DECREF(value);
            Py_DECREF(dict);
            PyErr_Format(PyExc_RuntimeError, "Failed to set dictionary item");
            return NULL;
        }

        Py_DECREF(key_str);
        Py_DECREF(value);

        while (json_str[pos] && isspace(json_str[pos]))
            pos++;

        if (json_str[pos] == '\0') {
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Expected another key-value pair of \"}\" symbol");
            return NULL;
        }

        if (json_str[pos] == ',') {
            pos++;
        }
        else if (json_str[pos] == '}') {
            return dict;
        }
        else {
            Py_DECREF(dict);
            PyErr_Format(PyExc_TypeError, "Expected object or value");
            return NULL;
        }
    }


    return dict;
}


static PyMethodDef cjson_methods[] = {
    // Определение доступных методов модуля
    {"loads", cjson_loads, METH_VARARGS, "Parse a JSON string and return a Python dictionary."},
    {"dumps", cjson_dumps, METH_VARARGS, "Serialize a Python dictionary into a JSON string."},
    {NULL, NULL, 0, NULL} };


static struct PyModuleDef cjson_module = {
    // Определение структуры модуля
    PyModuleDef_HEAD_INIT,
    "cjson",
    "A module for parsing and serializing JSON",
    -1,
    cjson_methods };


PyMODINIT_FUNC PyInit_cjson(void) {
    // Инициализация модуля
    return PyModule_Create(&cjson_module);
}