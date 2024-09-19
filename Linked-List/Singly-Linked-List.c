#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (!newNode) {
        printf("Memory error\n");
        return NULL;
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert value at the end
void insertNode(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

// Delete a node by value
void deleteNode(struct Node** head, int key) {
    struct Node *temp = *head, *prev;

    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        printf("Node with value %d deleted\n", key);
        return;
    }

    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Node with value %d not found\n", key);
        return;
    }

    prev->next = temp->next;
    free(temp);
    printf("Node with value %d deleted\n", key);
}

// Display the linked list
void displayList(struct Node* head) {
    struct Node* temp = head;
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    printf("Linked list: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

void maximumNode(struct Node* head) {
    struct Node* temp = head;
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    int max_value = temp->data;
    while (temp->next != NULL){
        if (temp->next->data > max_value){
            max_value = temp->next->data;
        }
        temp = temp->next;
    }
    printf("Max Value: %d", max_value);
}

void minimumNode(struct Node* head) {
    struct Node* temp = head;
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    int min_value = temp->data;
    while (temp->next != NULL){
        if (temp->next->data < min_value){
            min_value = temp->next->data;
        }
        temp = temp->next;
    }
    printf("Max Value: %d", min_value);
}

int main() {
    struct Node* head = NULL;
    int choice, value;

    while (1) {
        printf("\nMenu:\n");
        printf("1. Insert\n");
        printf("2. Delete node\n");
        printf("3. Display list\n");
        printf("4. Maximum\n");
        printf("5. Minimum\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert at beginning: ");
                scanf("%d", &value);
                insertNode(&head, value);
                break;
            case 2:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                deleteNode(&head, value);
                break;
            case 3:
                displayList(head);
                break;
            case 4:
                maximumNode(head);
                break;
            case 5:
                minimumNode(head);
                break;
            case 0:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }

    return 0;
}

