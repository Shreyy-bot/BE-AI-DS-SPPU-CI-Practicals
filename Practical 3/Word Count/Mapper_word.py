{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3e760ab8-ddf3-4796-828b-82551e52b241",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python3\n",
    "import sys\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "68e5ac4f-ca3e-4496-bacd-18416474c574",
   "metadata": {},
   "outputs": [],
   "source": [
    "for line in sys.stdin:\n",
    "    line = line.strip().lower()\n",
    "    words = re.findall(r'\\b\\w+\\b', line)\n",
    "    for word in words:\n",
    "        print(f\"{word}\\t1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f7d7767-807b-4e6f-b0c0-c8ccb1e201dd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
