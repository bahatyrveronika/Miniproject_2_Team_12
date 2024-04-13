def find_uniq(arr):
  """
  Kata link: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
  """
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    for key, value in freq.items():
        if value == 1:
            return key
