class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if len(tiles) == 1:
            return 1
        unique_chars = set()
        total_sequences = 0
        for index, char in enumerate(tiles):
            if char in unique_chars:
                continue
            unique_chars.add(char)
            total_sequences += 1 + self.numTilePossibilities(tiles[:index] + tiles[index+1:])
        return total_sequences
