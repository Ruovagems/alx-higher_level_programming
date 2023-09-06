#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    char *string;
    long int size, i, limit;

    setbuf(stdout, NULL);

    printf("[.] bytes object info\n");
    if (!PyBytes_CheckExact(p)) // Use PyBytes_CheckExact instead of PyBytes_Check
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        setbuf(stdout, NULL);
        return;
    }

    size = PyBytes_GET_SIZE(p); // Use PyBytes_GET_SIZE to get the size
    string = PyBytes_AS_STRING(p); // Use PyBytes_AS_STRING to get the string pointer

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = size < 10 ? size : 10; // Simplify limit calculation

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        printf(" %02x", (unsigned char)string[i]); // Cast to unsigned char for correct output

    printf("\n");
    setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints float information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_float(PyObject *p)
{
    double val;
    char *nf;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        setbuf(stdout, NULL);
        return;
    }

    val = PyFloat_AsDouble(p); // Use PyFloat_AsDouble to get the float value
    nf = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

    printf("  value: %s\n", nf);
    setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
    long int size, i;
    PyObject *obj;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        setbuf(stdout, NULL);
        return;
    }

    size = PyList_GET_SIZE(p); // Use PyList_GET_SIZE to get the list size

    printf("[*] Size of the Python List = %ld\n", size);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GET_ITEM(p, i); // Use PyList_GET_ITEM to get list items
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name); // Use Py_TYPE(obj) to get the type name

        if (PyBytes_CheckExact(obj))
            print_python_bytes(obj);
        if (PyFloat_Check(obj))
            print_python_float(obj);
    }
    setbuf(stdout, NULL);
}

