#include <Python.h>

// add function
static PyObject* add(PyObject* self, PyObject* args) {
    PyObject *a_obj, *b_obj;
    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj)) {
        return NULL;
    }
    double a, b;
    a = PyFloat_AsDouble(a_obj);
    if (a == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "First argument must be a number");
        return NULL;
    }
    b = PyFloat_AsDouble(b_obj);
    if (b == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "Second argument must be a number");
        return NULL;
    }
    return PyFloat_FromDouble(a + b);
}

// sub function
static PyObject* sub(PyObject* self, PyObject* args) {
    PyObject *a_obj, *b_obj;
    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj)) {
        return NULL;
    }
    double a, b;
    a = PyFloat_AsDouble(a_obj);
    if (a == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "First argument must be a number");
        return NULL;
    }
    b = PyFloat_AsDouble(b_obj);
    if (b == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "Second argument must be a number");
        return NULL;
    }
    return PyFloat_FromDouble(a - b);
}

// mul function
static PyObject* mul(PyObject* self, PyObject* args) {
    PyObject *a_obj, *b_obj;
    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj)) {
        return NULL;
    }
    double a, b;
    a = PyFloat_AsDouble(a_obj);
    if (a == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "First argument must be a number");
        return NULL;
    }
    b = PyFloat_AsDouble(b_obj);
    if (b == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "Second argument must be a number");
        return NULL;
    }
    return PyFloat_FromDouble(a * b);
}

// div function
static PyObject* divis(PyObject* self, PyObject* args) {
    PyObject *a_obj, *b_obj;
    // This format string "OO" means that two Python objects are expected as arguments, both of arbitrary type
    if (!PyArg_ParseTuple(args, "OO", &a_obj, &b_obj)) {
        return NULL;
    }
    double a, b;
    a = PyFloat_AsDouble(a_obj); // Convert a Python float object (a_obj) to a C double (a)
    if (a == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "First argument must be a number");
        return NULL;
    }
    b = PyFloat_AsDouble(b_obj);
    if (b == -1.0 && PyErr_Occurred()) {
        PyErr_SetString(PyExc_TypeError, "Second argument must be a number");
        return NULL;
    }
    if (b == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero");
        return NULL;
    }
    // This function creates a new Python float object with the value equal to the provided C double value
    // and returns a pointer to the object
    return PyFloat_FromDouble(a / b);
}

// method table
// METH_VARARGS means that the function takes a variable number of arguments passed as a tuple
static PyMethodDef CalculatorMethods[] = {
    {"add", add, METH_VARARGS, "Add two integers."},
    {"sub", sub, METH_VARARGS, "Subtract two integers."},
    {"mul", mul, METH_VARARGS, "Multiply two integers."},
    {"divis", divis, METH_VARARGS, "Divide two integers."},
    {0, 0, 0, 0} // This signals the end of the array
};

// module definition
static struct PyModuleDef calculatormodule = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    NULL, // A pointer to the module documentation
    -1, // The size of the per-module state
    CalculatorMethods
};

// module initialization
PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculatormodule);
}
