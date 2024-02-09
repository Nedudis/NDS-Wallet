#include <string.h>
#include <stdlib.h>
#include <stdio.h>

double GetPercentage(double a, double b) {
    double percentage = ((a - b) / 100.00);
    double result = b / percentage;
    return result;
}

void get_subname(const char *namearr[], size_t size, char* fixedarr[]) {
    for (int i = 0; i < size; i++) {    
        const char *str = namearr[i];
        size_t pos;
        size_t len = strlen(str);
        for(int j = 0; j < len; j++) {
            if(namearr[i][j] == '(') {
                pos = j;
                break;
            }
        }
        if (!pos == 0) {
            fixedarr[i] = (char*)malloc((pos + 1) * sizeof(char));
            strncpy(fixedarr[i], str, pos);
            fixedarr[i][pos] = '\0';
        } else {
            fixedarr[i] = (char*)malloc((len + 1) * sizeof(char));
            strcpy(fixedarr[i], str);
        }
    }
}