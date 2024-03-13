int value;
    if (index < len && index >= 0) {
        value = array[index];
    } else {
        printf("Invalid index\n");
        value = -1;
    }
    return value;
}