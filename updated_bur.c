char *buf = NULL;
size_t bufsize;

ares_status_t status = ares__read_line(fp, &buf, &bufsize);

if (status == ARES_SUCCESS) {
  // successfully read the line, process it as needed
  // ....
  ares_free(buf);  // don't forget to free the buffer 
}