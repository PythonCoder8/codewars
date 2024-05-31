int minRemove(std::vector<int> arr)
{
    if (arr.size() <= 1)
        return arr.size();
    std::sort(arr.begin(), arr.end());
    int result = arr.size() - 1;
    for (int i = 0; i < result; ++i)
    {
        auto square = arr[i] * arr[i];
        int current = i + std::distance(std::upper_bound(
            arr.begin() + i, arr.end(), square), arr.end());
        result = std::min(result, current);
    }
    return result;
}
