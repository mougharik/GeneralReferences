#ifndef _TEST_H
#define _TEST_H

#include <iostream>
#include <iomanip>
#include <ctime>
#include <vector>

namespace test
{
    void printList(const std::vector<int>& list)
    {
        int count = 1;
        for (auto i = list.cbegin(); i != list.cend(); i++)
        { 
            std::cout << std::setw(5) << *i;
            if (count % 10 == 0)
                std::cout << std::endl;
            count++;
        }
    }

    void fillList(std::vector<int>& list)
    {
        int size;
        std::cout << "\n Enter size of array: ";
        std::cin >> size;
        std::cout << std::endl;

        for (int i = 0; i < size; i++)
            list.push_back((rand() % 1000) + 1);
    }

    void beforeFormat(std::vector<int>& list)
    {
        std::cout << "Unsorted list: " << std::endl;
        printList(list);
        std::cout << "\n\n";
    }

    void afterFormat(std::vector<int>& list)
    {
        std::cout << "Sorted list: " << std::endl;
        printList(list);
        std::cout << "\n\n";
    }

}

#endif
