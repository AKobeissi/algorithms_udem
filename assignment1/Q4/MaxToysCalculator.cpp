#include "MaxToysCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe MaxToysCalculator
// this file contains the definitions of the methods of the MaxToysCalculator class

using namespace std;

MaxToysCalculator::MaxToysCalculator()
{
}

int MaxToysCalculator::CalculateMaxToys(const vector<int>& Toys, int S) {
   // ComplÃ©ter ici
   int n = Toys.size();
   int start = 0, end = 0;
   int currentSum = 0;
   int maxToys = 0;

    while (end < n) {
        currentSum += Toys[end];  // Expand the window to the right

        // If the current window sum exceeds the budget, shrink from the left
        while (currentSum > S && start <= end) {
            currentSum -= Toys[start];
            start++;
        }

        // Update max length of valid window
        maxToys = max(maxToys, end - start + 1);

        // Move end to the right to explore more
        end++;
    }

    return maxToys;
}
