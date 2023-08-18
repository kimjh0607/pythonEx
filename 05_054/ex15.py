import smartTv as st

my4kTv = st.Tv4k('65', 'grey', '4k')
my4kTv.turnOn()
my4kTv.turnOff()
my4kTv.setSmartTv('on')
my4kTv.printTvInfo()
print('-' * 20)

your4kTv = st.Tv4k('55', 'white', '4k')
your4kTv.setSmartTv('off')
your4kTv.turnOff()
your4kTv.turnOn()
your4kTv.printTvInfo()
print('-' * 20)

my8kTv = st.Tv8k('75', 'blue', '8k')
my8kTv.turnOn()
my8kTv.setSmartTv('on')
my8kTv.setAiTv('on')
my8kTv.printTvInfo()
print('-' * 20)

your8kTv = st.Tv8k('90', 'green', '8k')
your8kTv.turnOff()
your8kTv.setSmartTv('off')
your8kTv.setAiTv('off')
your8kTv.printTvInfo()
print('-' * 20)


