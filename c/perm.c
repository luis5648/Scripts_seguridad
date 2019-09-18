#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TAMANIO_ARRAY 7

bool a_array[] = {true, true, true, true, false, false, false, false};
bool b_array[] = {true, true, false, false, true, true, false, false};
bool c_array[] = {true, false, true, false, true, false, true, false};
bool d_array[TAMANIO_ARRAY];
bool e_array[TAMANIO_ARRAY];
bool f_array[TAMANIO_ARRAY];


void AlgoritmA()
{
    int k, j, i;
    char option;
    for (j = 0; j <= TAMANIO_ARRAY; j++)
    {
        printf("%i\n", d_array[j]);
    }
    getchar();
    printf("\nDesea continuar S/N?\n");
    scanf("%c", &option);

    switch (option)
    {
    case 'S':

        for (i = 0; i <= TAMANIO_ARRAY; i++)
        {
            if ((a_array[i]) && (b_array[i]))
            {
                d_array[i] = true;
            }
            else
            {
                d_array[i] = false;
            }
        }

        for (j = 0; j <= TAMANIO_ARRAY; j++)
        {
            if (!(a_array[j]) && (c_array[j]))
            {
                e_array[j] = true;
            }
            else
            {
                e_array[j] = false;
            }
        }

        for (k = 0; k <= TAMANIO_ARRAY; k++)
        {
            if ((d_array[k]) || (e_array[k]))
            {
                f_array[k] = true;
            }
            else
            {
                f_array[k] = false;
            }
        }
     
        printf("-------------------------\n");
        break;
    case 'N':
        getchar();
        printf("Saliendo ...");
        getchar();
        system("cls");
        exit(0);
        //NULL CODE !!!
        break;
    default:
        printf("Error an ocurred, try again...\n");
        system("cls");
    }
}

void mainMenu()
{
    int opc = 0;

    do
    {
        printf("Seleccione una opcion\n");
        printf("1.- Algoritmo 1\n");
        printf("2.-Algoritmo 2\n");
        printf("3.- Salir\n");
        scanf("%d", &opc);
        system("cls");
        switch (opc)
        {
        case 1:
            AlgoritmA();
            break;
        case 2:

            break;
        case 3:
            printf("Saliendo...");
            exit(0);
            break;
        default:
            printf("An ocurred error, try again..\n");
            system("cls");
        }

    } while (opc = 3);
}

int main()
{

    mainMenu();
    return 0;
}
