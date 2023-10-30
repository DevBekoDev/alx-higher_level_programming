#include "lists.h"

/**
 * check_cycle - checks for single linked lists
 * @list: pointer.
 * Return: 0 no cycle, 1 there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *list1 = NULL;
	listint_t *list2 = NULL;

	if (list == NULL)
		return (0);
	list1 = list;
	list2 = list;

	while (list1 && list2 && list2->next)
	{
		list1 = list1->next;
		list2 = list2->next->next;

		if (list1 == list2)
			return (1);
	}
	return (0);
}
