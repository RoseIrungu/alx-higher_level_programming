#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int a;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %la\n", size);
	printf("[*] Allocated = %la\n", obj->allocated);
	for (a = 0; a < size; a++)
		printf("Element %a: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}
