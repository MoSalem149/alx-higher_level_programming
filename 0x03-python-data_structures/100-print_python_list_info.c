#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  func that prints some basic info
 * Description: 100-print_python_list_info.c task
 * @p: py list
 */
void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}
