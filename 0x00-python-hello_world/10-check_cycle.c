#include "lists.h"

/**
 * check_cycle - Checks is the list its a cycle.
 * @list: Pointer to the list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
  listint_t *slow = list, *fast = list;

  if (list == NULL)
    {
      return (0);
    }
  
  while (slow && fast && fast->next)
    {
      slow = slow->next;
      fast = fast->next->next;
      
      if (slow == fast)
	{
	  return (1);
	}
    }
  return (0);
}
