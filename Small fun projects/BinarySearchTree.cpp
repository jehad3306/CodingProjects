#include <iostream>
#include <string>

struct node {
    int key;
    struct node* left;
    struct node* right;
};

node* createNode(int key) {
    node* Node = new node();
    Node->key = key;
    Node->left = NULL;
    Node->right = NULL;
    return Node;
}

bool nodeFound(int position) {
    return position != -1;
}

int findDepth(node* root, int x) {
    if (root == NULL) {
        return -1;
    }

    int dist{ -1 };
    if (root->key == x) {
        return dist + 1;
    }
    else if ((dist = findDepth(root->left, x)) >= 0) {
        return dist + 1;
    }
    else if ((dist = findDepth(root->right, x)) >= 0) {
        return dist + 1;
    }

    return dist;
}

void nodeValue(node* root) {
    if (root == NULL)
        return;

    std::cout << root->key << " ";
    nodeValue(root->left);
    nodeValue(root->right);
}

struct node* insertNode(struct node* node, int x) {
    if (node == NULL)
        return createNode(x);

    if (x < node->key) {
        node->left = insertNode(node->left, x);
    }
    else if (x > node->key) {
        node->right = insertNode(node->right, x);
    }

    return node;
}

int main() {
    // Root
    node* root = createNode(8);
    // Left Branch
    root->left = createNode(3);
    root->left->left = createNode(1);
    root->left->right = createNode(6);
    root->left->right->left = createNode(4);
    root->left->right->right = createNode(7);
    // Right Branch
    root->right = createNode(10);
    root->right->right = createNode(14);
    root->right->right->left = createNode(13);

    int x;
    std::cout << "Write a value to check if it's in the tree. If not, we will create a new node.\nValue: ";
    std::cin >> x;

    int search{ findDepth(root, x) };
    std::cout << search << std::endl;
    std::cout << "If the value is 0, it's not found. If it's 1, it's true: " << nodeFound(search) << std::endl;

    if (!nodeFound(search)) {
        insertNode(root, x);
        std::cout << "Created a leaf node with the value: " << x << std::endl;
    }

    nodeValue(root);
    return 0;
}
