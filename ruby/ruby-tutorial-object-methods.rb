def odd_or_even(number)
    if number % 2
        return number.even?
    else 
        return number.odd?
    end
end

(0...gets.to_i).each do |i|
    puts odd_or_even(gets.to_i)
end
