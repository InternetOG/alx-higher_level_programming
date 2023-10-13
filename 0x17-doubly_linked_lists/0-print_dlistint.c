#include "lists.h"
/**
 * print_dlistint - prints the length of a doubly linked list
 * @h: The head node
 *
 * Return: returns the number in lenght
 */
size_t print_dlistint(const dlistint_t *h)
{
size_t n = 0;

if (h != NULL)
{
while (h != NULL)
{
n += 1;
h = h->next;
}
return (n);
}
return (n);
}
