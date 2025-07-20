#Stock Buy and Sell - Max one Transaction Allowed
#“If I sell now, what’s the profit compared to the best buy price so far?”
# prices =[7,10,1,3,6,9,2]

def maxprofit(prices):
    minsofar=prices[0]
    maxprofit=0

    for i in range(1,len(prices)):
        minsofar=min(minsofar,prices[i])
        maxprofit=max(maxprofit,prices[i]-minsofar)
    return maxprofit

if __name__ == "__main__":
    prices =[7,10,1,3,6,9,2]
    print(maxprofit(prices))  # Output: 8 (Buy at 1, Sell at 9)
 #Input: prices[] = {7, 6, 4, 3, 1} 
#output 0
#explanation:rray is sorted in decreasing order, 0 profit can be made without making any transaction.
