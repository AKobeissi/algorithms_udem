#ifndef CAREERCALCULATOR_H
#define CAREERCALCULATOR_H

#include <vector>

// ce fichier contient les declarations des methodes de la classe CareerCalculator
// peut être modifié si vous voulez ajouter d'autres méthodes à la classe
// this file contains the declarations of the methods of the CareerCalculator class
// can be modified if you wish to add other methods to the class

// This class implements a function to determine whether the objective (i.e. 
// reaching the end of the vector) is achievable given a sequence of steps.
class CareerCalculator {
public:
    CareerCalculator();
    // Returns true if it is possible to reach the last index, false otherwise.
    bool CalculateMaxCareer(const std::vector<int>& Steps);
};

#endif // CAREERCALCULATOR_H


