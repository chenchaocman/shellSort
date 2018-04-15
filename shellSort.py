 # -*- coding: utf-8 -*-    


def ShellSort(arry):

	n = len(arry)

	gap = n//2#规定间距(gap每次都缩短为原来的一般)

	while gap>=1:

		for j in xrange(gap,n):

			i = j

			while (i-gap)>=0:#一定要加上==0，因为要考虑gap==1 和 i==1的时候
						#使数组中的  间隔为gap的元素互相比较 。当gap为1的时候，实际上就是插入算法
				if arry[i]<arry[i-gap]:
					arry[i-gap],arry[i] = arry[i],arry[i-gap]
					i=i-gap
				else:
					break	


		gap = gap//2



if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20,99]
    ShellSort(alist)
    print("aaa")
    print(alist)

				
			




