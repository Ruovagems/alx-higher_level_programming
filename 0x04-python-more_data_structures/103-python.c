#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *byte_obj = (PyBytesObject *)p;
    Py_ssize_t size;
    Py_ssize_t i;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(byte_obj)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes:", (size < 10) ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf(" %02x", byte_obj->ob_sval[i] & 0xff);
    }
    printf("\n");
}

