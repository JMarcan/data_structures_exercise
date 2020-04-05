import hashlib
from datetime import datetime

  
class Block:

    def __init__(self, timestamp, data_hash, previous_hash, index):
      """
        Initialize one blockchain Block 
    
        Args:
            - timestamp(str): timestamp
            - data_hash(str): hashed data to be stored
            - previous_hash(str): hash of the previous block
            - index(int): index of a block

        Returns:
            - None
      """
      self.timestamp = timestamp
      self.hash = data_hash
      self.previous_hash = previous_hash
      self.index = index
      
    def __repr__(self):
        return str.format("\nThis is a block with an index: \'{0}\', timestamp:\'{1}\', \
                          hash: \'{2}\', previous hash: \'{3}\'\n \
                          ".format(self.index, self.timestamp, self.hash, self.previous_hash))
  
class Blockchain:
    
    def __init__(self, name):
        """
        Initialize a blockchain 
    
        Args:
            - name(str): name of the blockchain

        Returns:
            - None
      """
        self.name = name
        
        self.last_block_idx = 0
        self.previous_hash = None
    
    def calc_hash(self, hash_str):
      sha = hashlib.sha256()
     
      sha.update(hash_str.encode('utf-8'))
      
      return sha.hexdigest()
  
    def add_block(self, data):
        self.last_block_idx += 1
        data_hash = self.calc_hash(data)
        b = Block(datetime.now(), data_hash, self.previous_hash, self.last_block_idx)
        self.blocks.append(b)
        self.previous_hash = data_hash
        
      
if __name__ == '__main__':
    blockchain = Blockchain("My Blockchain")
    
    blockchain.add_block("First Block")
    blockchain.add_block("Second Block")
    blockchain.add_block("Third Block")
    
    for block in blockchain.blocks:
        print (block)

    
    