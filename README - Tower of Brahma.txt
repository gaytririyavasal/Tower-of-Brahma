
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

The puzzle Tower of Hanoi was introduced in 1883. It consisted of three pegs fastened to a stand. There were eight circular disks of wood, each of which had a hole in the middle through which a peg could be passed. These disks were of different radii, and initially, they were all placed on one of the pegs, with the biggest disk on the bottom and successively smaller disks on the top.

The problem was to shift all of the disks from the initial peg to any other peg according to the following two rules:

1. Only one disk could be moved at a given time.
2. At no time could a larger disk be on top of a smaller disk.

This puzzle came with a story that was published by De Parville in La Nature, Paris, 1884, pp. 285-286.

"De Parville gave an account of the origin of the toy which is a sufficiently pretty idea to deserve repetition. In the great temple at Benares, says he, beneath the dome which marks the centre of the world, rests a brass plate in which are fixed three diamond needles, each a cubit high and as thick as the body of a bee. On one of these needles, at the creation, God, placed sixty-four disks of pure gold, the largest disk resting on the brass plate, and the others getting smaller and smaller up to the top one. This is the Tower of Brahma. Day and night unceasingly the priests transfer the disks from one diamond needle to another according to the fixed and immutable laws of Brahma, which require that the priest on duty must not move more than one disk at a time and that he must place this disk on a needle so that there is no smaller disk below it. When the sixty four disks shall have been thus transferred from the needle on which at the creation God placed them to one of the other needles, tower, temple, and Brahmins alike will crumble into dust, and with a thunderclap the world will vanish."

The number of separate transfers of single disks which the priests must make to effect the transfer of the tower is 264 - 1, that is 18,446,744,073,709,551,615. If each transfer takes 1 second, then the time taken is 585 billion years where our current estimate of the age of the universe is 13.8 billion years.

This was going on for eons until one day one of the priests who was more computationally minded than the others informed his fellow-priests that they could achieve the transfer in a single afternoon at the one disk-per-second rhythm by using an additional needle. He proposed the following strategy having four needles - source, spare1, spare2, and destination.

- First, move the topmost disks (say the top k disks) to one of the spare needles, say spare1.
- Then, move n - k - 1 disks to spare2.
- Move the largest disk from source to destination.
- Move the n - k - 1 disks from spare2 to destination.
- Finally, move the top k disks from spare1 to destination.

He calculated the value of k which minimized the number of movements and found that 18,433 transfers would suffice. Thus they could spend just 5 hours, 7 minutes, and 13 seconds with this scheme versus 585 billion years without the additional needle.

Implement this priest / computational scientist's algorithm. The value of k that minimizes the number of transfers is

k = n - √(2 * n + 1) + 1

Use this value of k to compute the total number of transfers using four needles where the priest can move only one disk at a time and must place each disk on a needle such that there is no smaller disk below it.

Input: 

You must read the input file from stdin. The input file contains several lines of input. Each line contains a single integer 0 ≤ N ≤ 10,000, giving the number of disks to be transferred. Input is terminated by the end of the file.

1
2
28
64

Output: 

For each line of input, produce one line of output which indicates the number of movements required to transfer N disks to the final needle using four needles. For the above input file, the output will be:

1
3
769
18433

In the function main(), you will read the number of disks from a file called tower.in. Assume that the number of disks is between 0 and 10000 inclusive. You do not have to do any error checking.
