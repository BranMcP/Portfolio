/*
* 
* Branigan McPeters
* bmcpeter@my.athens.edu
* 00083473
* CS 417
* 09/03/2022
*
* Assignment Two Question 2: Create a BST with 1000 random numbers 
* and then search for those 1000 random numbers in the tree
*
* Sample Code Source:
* https://codereview.stackexchange.com/questions/191211/binary-search-tree-data-structure-implementation-in-c11-using-smart-pointers
*/

#include <random>
#include <functional>
#include <ctime>
#include <vector>

#include "bst.h"

int main() {
  BST <int> binary_search_tree;
  std::vector<int> random_numbers;

  // Random Number Generator
  std::default_random_engine gen((unsigned int)std::time(0));	
  std::uniform_int_distribution<int> distribution(1, 1000);
  auto randInt = std::bind(distribution, gen);

  for(int index = 0; index < 999; ++index){
    random_numbers.push_back(randInt());
    binary_search_tree.insert(random_numbers[index]);
  }


  for(int index = 999; index > 0; --index){
    if(binary_search_tree.search(random_numbers[index])){
      std::cout << "FOUND: " << random_numbers[index] << "\n";
    }
  }


  //binary_search_tree.traverse_tree([](auto Node){ std::cout << Node->data << std::endl; });

  return 0;
}