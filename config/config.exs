import Config

config :advent_of_code_utils,
  auto_compile?: true,
  time_calls?: true,
  gen_tests?: true,
  session: System.get_env("AOC_TOKEN")

config :iex,
  inspect: [charlists: :as_lists]
