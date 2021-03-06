
/*	=============================================================================
 *	Polonator G.007 Selective Release Software
 *
 *   Wyss Institute Harvard Medical School
 *   Written by Nick Conway
 *
 *   Illuminate_common.c: common functions that allow for illumination mask generation
 *
 *   Original version --                07-22-2010 [NC]]
 *
 *   This software may be modified and re-distributed, but this header must appear
 *   at the top of the file.
 *
 *	=============================================================================
*/
#include "illuminate_common.h"
#include <stdio.h>
#include <stdlib.h>


IlluminateMask illum_allocate_mask(void)
{
    int i;
    IlluminateMask mask;
    //mask = malloc(ILLUMINATEMASK_COL_LEN*sizeof(IlluminateMask));
    mask = malloc(ILLUMINATEMASK_COL_LEN*sizeof(IlluminateMask_row)); //
    if(mask == NULL)
    {
	printf("out of memory\n");
	exit(0);
    }
    for(i = 0; i < ILLUMINATEMASK_COL_LEN; i++)
    {
	//mask[i] = malloc(ILLUMINATEMASK_ROW_LEN * sizeof(IlluminateMask_row));
	mask[i] = malloc(ILLUMINATEMASK_ROW_LEN);
        if(mask[i] == NULL)
	{
            printf("out of memory\n");
            exit(0);
	}
    }
    return mask;
}

int illum_free_mask(IlluminateMask mask)
{
    int i;
    for(i = 0; i < ILLUMINATEMASK_COL_LEN; i++)
    {
	free(mask[i]);
    }
    free(mask);
    return 1;
}
