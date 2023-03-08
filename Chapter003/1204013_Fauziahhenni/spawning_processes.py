#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def myFunc(i):
    print ('Karyawan Mengerjakan Tugas : %s' %i)
    for j in range (0,i):
        print('Tugas diselesaikan Karyawan :%s' %j)
    return

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()