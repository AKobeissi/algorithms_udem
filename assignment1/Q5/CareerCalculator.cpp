#include "CareerCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe CareerCalculator
// this file contains the definitions of the methods of the CareerCalculator class

using namespace std;

CareerCalculator::CareerCalculator()
{
}

bool CareerCalculator::CalculateMaxCareer(const vector<int>& Steps) {
    // Completer ici
    int n = Steps.size();
    int farthest = 0;

    for (int i = 0; i < n; i++) {
        if (i > farthest) {
            // If we've reached a point we can't jump to, we fail
            return false;
        }
        farthest = max(farthest, i + Steps[i]);
        if (farthest >= n - 1) {
            return true;
        }
    }

    return false;
}