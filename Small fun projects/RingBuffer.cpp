
// Ringbuffer is a data structure which utilizes FIFO with a fixed size. 
// If it is full, the head pointer will rewrite over the oldest data inserted.
// Mutex ( mutual exclusion ) is about preventing the same resource at the same time. 
// If thread 1 tries to acces the memory or the source it will lock the other thread from trying to get the resource and vice versa.


// Mutex locks is about preventing threads from getting into the same resource at the same time so they use a method called mutex locks.
// If a thread acces the source, it will unlock it if no one else is using it,
// if another thread tries to get to it, the path will be locked so the thread will be blocked from accesing the source.

// Synchronization is about finishing off a task given to a thread before allowing another thread to finish of theirs task. 
//When the first thread is done, it has to inform to the next thread, that i am done so he can start.

#include <iostream>
#include <string>
#include <thread>
#include <mutex>
#include <Windows.h>

class RingBuffer {
public:
    RingBuffer(int capacity) {
        buffer = new char[capacity];
        bufferSize = capacity;
    }

    ~RingBuffer() {
        if (buffer != nullptr) {
            delete[] buffer;
        }
    }

    void add(char val) {
        while ((in + 1) % bufferSize == out);
        buffer[in] = val;
        std::lock_guard<std::mutex> lock(A);
        in = (in + 1) % bufferSize;
    }

    char get() {
        while (in == out);
        std::lock_guard<std::mutex> lock(A);
        int consumed = buffer[out];
        out = (out + 1) % bufferSize;
        return consumed;
    }

private:
    char* buffer;
    std::mutex A;
    int bufferSize;
    int in = 0;
    int out = 0;
};

void bufferReader(RingBuffer* buffer) {
    while (true) {
        std::cout << buffer->get();
    }
}

void keyboardReader(RingBuffer* buffer) {
    while (true) {
        std::string input;
        std::getline(std::cin, input);

        for (char c : input) {
            buffer->add(c);
        }
        buffer->add('\n');
    }
}

void generator(RingBuffer* buffer) {
    std::string characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (int i = 0; i < 10; i++) {
        int random = rand() % characters.size();
        char tekstData = characters[random];
        buffer->add(tekstData);
        Sleep(1000);
    }
}

int main() {
    const int bufferCapacity = 10;
    RingBuffer buffer(bufferCapacity);

    std::thread generatorThread(generator, &buffer);
    std::thread keyboardThread(keyboardReader, &buffer);
    std::thread readerThread(bufferReader, &buffer);

    generatorThread.join();
    keyboardThread.join();
    readerThread.join();

    return 0;
}
