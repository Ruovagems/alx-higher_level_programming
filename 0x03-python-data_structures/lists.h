ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
def delete_at(my_list=[], idx=0);
def divisible_by_2(my_list=[]):
def max_integer(my_list=[]):
def multiple_returns(sentence):
def add_tuple(tuple_a=(), tuple_b=()):
def print_matrix_integer(matrix=[[]]):
def no_c(my_string):
def new_in_list(my_list, idx, element):
def print_reversed_list_integer(my_list=[]):
def replace_in_list(my_list, idx, element):
def element_at(my_list, idx):
def print_list_integer(my_list=[]):

int is_palindrome(listint_t **head);
void print_python_list_info(PyObject *p);

#endif /* LISTS_H */
