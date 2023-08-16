#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
	int n;
	struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head);

int is_palindrome(listint_t **head) {
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL) {
		while (fast != NULL && fast->next != NULL) {
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL) {
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;

		listint_t *prev = NULL;
		listint_t *current = second_half;
		listint_t *next_node;

		while (current != NULL) {
			next_node = current->next;
			current->next = prev;
			prev = current;
			current = next_node;
		}

		second_half = prev;

		listint_t *list1 = *head;
		listint_t *list2 = second_half;

		while (list2 != NULL) {
			if (list1->n != list2->n) {
				is_palindrome = 0;
				break;
			}
			list1 = list1->next;
			list2 = list2->next;
		}

		prev = NULL;
		current = second_half;
		next_node = NULL;

		while (current != NULL) {
			next_node = current->next;
			current->next = prev;
			prev = current;
			current = next_node;
		}
		prev_slow->next = prev;
	}

	return is_palindrome;
}

int main() {
	listint_t *head = NULL;
	listint_t *new_node;

	int result = is_palindrome(&head);
	if (result) {
		printf("The linked list is a palindrome.\n");
	} else {
		printf("The linked list is not a palindrome.\n");
	}

	return 0;
}

