#ifndef _QUICKSORT_H
#define _QUICKSORT_H

#include <vector>
#include <utility>
#include "insertionsort.h"

namespace quicksort 
{

    int partition(std::vector<int>& array, int start, int end)
    {   
        
        int mid = (start + end) / 2;
        
        if (array[mid] < array[start])
            std::swap(array[mid], array[start]);
        if (array[start] < array[end])
            std::swap(array[start], array[end]);
        if (array[end] < array[mid])
            std::swap(array[mid], array[end]);

        std::swap(array[mid], array[end]);
        
        int pivot = array[end];
        int i = start;
        int j = end-1;
        while (i <= j)
        {
            while (i <= j && array[i] <= pivot)
                i++;
            while (i <= j && array[j] > pivot)
                j--;
            if (i < j)
                std::swap(array[i], array[j]);
            else
                break;
        }

        std::swap(array[i], array[end]);
        return i;
    }


    void quicksort(std::vector<int>& array, int start, int end)
    {
        if (start + 20 < end)
        {
            int pivot = partition(array, start, end);
            quicksort(array, start, pivot-1);
            quicksort(array, pivot+1, end);
        }
        else
            isort::insertionSort(array);
    }

}

#endif
