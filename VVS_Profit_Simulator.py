import matplotlib.pyplot as plt


############ Param #############
# Note that the time unit is day
DAY = 1
WEEK = 7
MONTH = 30
YEAR = 365
REINVEST_INTERVAL_UNIT = DAY
INITIAL_CAPITAL = 1283.0
APR_PERCENTAGE = 31.49
SIMULATION_LENGTH = YEAR
################################


class VVS_Simulator():
    def __init__(self, init_capital, apr, reinvest_interval, \
                swap_fee_rate=0.003, reinvest_fix_cost=2.3, harvest_collect_fee=1.0, remove_LP_fee=2.0):
                #  swap_fee_rate=0.0, reinvest_fix_cost=0.0, harvest_collect_fee=0.0, remove_LP_fee=0.0):
        '''
        time unit = day
        '''
        self.harvest = 0.0
        self.t = 0
        
        self.init_capital = init_capital
        self.capital = init_capital
        self.dpr = apr / YEAR # day percentage rate
        self.reinvest_interval = reinvest_interval
        self.swap_fee_rate = swap_fee_rate
        self.reinvest_fix_cost = reinvest_fix_cost
        self.harvest_collect_fee = harvest_collect_fee
        self.remove_LP_fee = remove_LP_fee

    def tick(self):
        '''
        simulate 1 day is past
        '''
        self.harvest += self.dpr * self.capital
        self.t += 1
        if self.t % self.reinvest_interval == 0:
            self.reinvest()

    def reinvest(self):
        earning = self.harvest - self.reinvest_fix_cost - self.harvest * 0.5 * self.swap_fee_rate
        self.harvest = 0.0
        self.capital += earning
    
    def calculate_earning(self):
        total_earned = self.capital - self.init_capital
        if self.harvest > self.harvest_collect_fee:
            total_earned += self.harvest - self.harvest_collect_fee
        total_earned -= self.remove_LP_fee
        return total_earned


simulators = []
reinvest_interval = []
for interval in range(2*WEEK, 11*MONTH, REINVEST_INTERVAL_UNIT):
    reinvest_interval.append(interval)
    simulators.append(
        VVS_Simulator(
            init_capital=INITIAL_CAPITAL, 
            apr=APR_PERCENTAGE/100.0, 
            reinvest_interval=interval))
for t in range(0, SIMULATION_LENGTH, REINVEST_INTERVAL_UNIT):
    for s in simulators:
        s.tick()
    print('progress:', t, '/', SIMULATION_LENGTH)
earnings = list(map(
    lambda s: round(s.calculate_earning(), 2), simulators))

reinvest_interval_earning_pairs = list(zip(reinvest_interval, earnings))
best_earning_pair = max(reinvest_interval_earning_pairs, key=lambda x: x[1])

title = "With init cap %.2f USD and APR %.2f%%,\n " + \
        "best reinvest interval is every %d days \n" + \
        " which yields %.2f USD profits in %d days."
title = title % (INITIAL_CAPITAL, APR_PERCENTAGE, best_earning_pair[0], best_earning_pair[1], SIMULATION_LENGTH)
print(title)

plt.plot(reinvest_interval, earnings)
plt.suptitle(title)
plt.tight_layout()
plt.show()