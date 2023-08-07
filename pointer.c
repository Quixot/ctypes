#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char* alloc_memory() {
    char* str = strdup("Hello, World!");
    printf("memory allocated...\n");
    return str;
}


void free_memory(char* ptr) {
    printf("memory free...\n");
    free(ptr);
}


char* alloc_memory_with_malloc() {
   char *str;

   /* Initial memory allocation */
   str = (char *) malloc(15);
   strcpy(str, "tutorialspoint");
   printf("String = %s,  Address = %p\n", str, str);

   /* Reallocating memory */
   str = (char *) realloc(str, 25);
   strcat(str, ".com");
   printf("String = %s,  Address = %p\n", str, str);

   free(str);
   
   return(0);
}

