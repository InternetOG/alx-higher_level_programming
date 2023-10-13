#include "lists.h"
/**
 * dlistint_len - prints the length of a doubly linked list
 * @h: The head node
 *
 * Return: returns the number in lenght
 */
size_t dlistint_len(const dlistint_t *h);
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
