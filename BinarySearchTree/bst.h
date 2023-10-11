#ifndef BST_H
#define BST_H

#include <iostream>
#include <algorithm>
#include <memory>
using std::cout;

template <typename D>
class BST {
private:
  struct Node {
    D data;
    std::weak_ptr<Node> previous;
    std::shared_ptr<Node> left;
    std::shared_ptr<Node> right;

    Node(const D data) {
      this->data = data;
      this->previous.reset();
      this->left = nullptr;
      this->right = nullptr;
    }
  };

  std::shared_ptr<Node> root;

  void traverse_tree(std::shared_ptr<Node> &tempRoot, void handler(std::shared_ptr<Node>)) {
    if (tempRoot == nullptr) return;
    traverse_tree(tempRoot->left, handler);
    handler(tempRoot);
    traverse_tree(tempRoot->right, handler);
  }

public:
  BST() {
    root = nullptr;
  }

  ~BST() {}

  const bool isEmpty() {
    return(root == nullptr);
  }

  void traverse_tree(void handler(std::shared_ptr<Node>)) {
    traverse_tree(root, handler);
  }

  void insert(const D data) {
    std::shared_ptr<Node> current = root;
    std::shared_ptr<Node> previous = nullptr;
    while(current!=nullptr) {
      previous = current;
      if (data > current->data) {
        current = current->right;
      } else if (data < current->data) {
        current = current->left;
      } else {
        return nullptr;
      }
    }
    current = std::make_shared<Node>(data);
    current->previous = previous;
    if(previous == nullptr) {
      root = current;
    } else if (current->data > previous->data) {
      previous->right = current;
    } else if (current->data < previous->data) {
      previous->left = current;
    }
    return current;
  }

  bool search(const D data) {
    std::shared_ptr<Node> tempRoot = root;
    while (tempRoot != nullptr) {
      if (data > tempRoot->data) {
        tempRoot = tempRoot->right;
      } else if (data < tempRoot->data) {
        tempRoot = tempRoot->left;
      } else {
        return true;
      }
    }
    return false;
  }

};

#endif