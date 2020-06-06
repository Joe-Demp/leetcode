# Note the solution is incorrect
class Solution
=begin
    :type w: Integer[]
=end
    def initialize(w)
        @rando = Random.new
        @sums = Array.new(w.length)
        @sums[0] = w[0]

        1.upto(w.length - 1) do |i|
            @sums[i] = sums[i - 1] + w[i]
        end

        @total_sum = @sums[w.length - 1]
    end

=begin
    :rtype: IntegerBalls
=end
    def pick_index()
        j = @rando.rand(@total_sum)
        left = 0
        right = @sums.length - 1

        until left == right - 1 do
            median = (left + right) / 2

            if @sums[median] <= j
                left = median
            elsif @sums[median] > j
                right = median
            end
        end
        left
    end
end

# Strategy: 

# initialize is called. Calculate a cumulative sum array of 'w'. Record the total sum as the number of elements in an expanded array
# i.e. weight_sums
# i.e. if the weight of 0 is 5, the expanded array would begin as: [0, 0, 0, 0, 0, ...]

# pick_index is called
# generate a random number between 0 and the length of the expanded array: k
# goal, to find the number that expanded_weights[k] would point to if expanded weights existed
# Find a point in the array where weight_sums[i] <= k and k < weight_sums[i + 1]
# The index to return is then i
