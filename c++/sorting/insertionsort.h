#ifndef _INSERTIONSORT_H
#define _INSERTIONSORT_H

#include <vector>

namespace isort
{
    void insertionSort(std::vector<int>& array)
    {
        for (int i = 0; i < array.size(); i++)
        {
            for (int j = i; j > 0 && array[j] < array[j-1]; j--)
            {
                int temp = array[j];
                array[j] = array[j-1];
                array[j-1] = temp;
            }
        }
    }
}
#endif
