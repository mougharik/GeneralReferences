#include <iostream>
#include <iomanip>
#include <ctime>
#include <vector>
#include "test.h"
#include "insertionsort.h"

int main()
{
    std::cout << "Insertion Sort Test" << std::endl;
    
    std::vector<int> array;
    test::fillList(array);
    
    test::beforeFormat(array);

    clock_t time = clock();
    isort::insertionSort(array);
    time = clock() - time;
    float seconds = static_cast<float>(time) / CLOCKS_PER_SEC;
    
    test::afterFormat(array);

    std::cout << std::setiosflags(std::ios::fixed);
    std::cout << "Time took to sort " << array.size() << " elements: " << seconds << " seconds\n";

    return 0;
}


