

from src.services.timer import timer


class Sort:

    def cmpcount(cmp):
        """
        Function is auxiliary and is used only as a measurement of the work of algorithms
        """
        cmp[0] += 1
        return True

    @timer
    def shell(list, field):
        swp = 0
        cmp = [0]
        last_index = len(list)
        step = len(list)//2
        while step > 0:
            for i in range(step, last_index):
                tmp = i
                delta = tmp - step
                while delta >= 0 and Sort.cmpcount(cmp) and getattr(list[delta], field) > getattr(list[tmp], field):
                    swp +=1
                    list[delta], list[tmp] = list[tmp], list[delta]
                    tmp = delta
                    delta = tmp - step
            step //= 2
        return (list, swp, cmp[0])

    @timer
    def quickSort(list, field):

        def qsort(list, field, low, high):

            def partition(list, field, low, high):
                pivot = getattr(list[high], field)
                i = low - 1
                for j in range(low, high):
                    if Sort.cmpcount(cmp) and getattr(list[j], field) <= pivot:
                        i = i + 1
                    (list[i], list[j]) = (list[j], list[i])
                    swp[0] +=1
                (list[i + 1], list[high]) = (list[high], list[i + 1])
                swp[0] +=1
                return i + 1

            if low < high:
                pi = partition(list, field, low, high)
                qsort(list, field, low, pi - 1)
                qsort(list, field, pi + 1, high)
            return list
        swp = [0]
        cmp = [0]
        return (qsort(list, field, 0, len(list)-1), swp[0], cmp[0])


    @timer
    def mergeSort(list, field):

        def msort(list, field):
            if len(list) > 1:

                r = len(list)//2
                L = list[:r]
                M = list[r:]

                msort(L, field)
                msort(M, field)

                i = j = k = 0

                while i < len(L) and j < len(M):
                    if Sort.cmpcount(cmp) and getattr(L[i], field) < getattr(M[j], field):
                        list[k] = L[i]
                        i += 1
                    else:
                        list[k] = M[j]
                        j += 1
                    swp[0] += 1
                    k += 1

                while i < len(L):
                    list[k] = L[i]
                    i += 1
                    k += 1
                    swp[0] += 1

                while j < len(M):
                    list[k] = M[j]
                    j += 1
                    k += 1
                    swp[0] += 1

            return list
        swp = [0]
        cmp = [0]
        return (msort(list, field), swp[0], cmp[0])