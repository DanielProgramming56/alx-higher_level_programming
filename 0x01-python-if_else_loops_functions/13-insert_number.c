#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list.
* @head: the head of the node
* @number: value to be inserted
* Return: new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;
	listint_t *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	current = *head;
	prev = NULL;
	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = prev->next;
		prev->next = new_node;
	}
	return (new_node);
}
