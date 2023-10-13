#include "lists.h"
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
        return n;
    }
    return n;
}
