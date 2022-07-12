local function filter(input, env)
  local skip = string.len(env.engine.context.input) ~= 4
  local candidates = {}
  local del_text = {}
  local index_text = {}
  local chinese_count = 0
  for cand in input:iter() do
    if not skip then
      table.insert(index_text, cand.text)
      candidates[cand.text] = cand
      if (string.byte(cand.text, 1) > 127) then
        chinese_count = chinese_count + 1
      else
        table.insert(del_text, cand.text)
      end
    else
      yield(cand)
    end
  end
  if chinese_count == 1 then
    for i, t in pairs(del_text) do
      candidates[t] = nil
    end
  end
  for i, t in pairs(index_text) do
    if candidates[t] ~= nil then
      yield(candidates[t])
    end
  end
end

return filter
