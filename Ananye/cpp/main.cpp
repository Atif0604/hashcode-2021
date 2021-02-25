#include <bits/stdc++.h>

using namespace std;

#define fio ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(0);
#define LL long long int
#define ULL unsigned long long int
#define VI vector<int>
#define VLL vector<LL>
#define VLIT VLL::iterator
#define SLL set<LL>
#define PB push_back
#define MAXD 1004
#define REP(i, n) for(int i = 1; i <= n; i++)
#define REPZ(i, n) for(int i = 0; i < n; i++)
#define REPI(i, a, b) for(int i = a; i <= b; i++)
#define LD long double
#define PI pair<int, int>
#define PLL pair<LL, LL>
#define VPI vector<PI>
#define VPL vector<PLL>
#define ALL(x) x.begin(), x.end()
#define F first
#define S second
#define PB push_back
#define POB pop_back
#define MP make_pair
#define PIPI pair<PI, int>
#define VPIPI vector<PIPI>
#define SI set<int>
#define INS insert
#define LD long double
#define VVL vector<VLL>
#define PF push_front
#define MCU map<LL, VI> 
#define LD long double
#define QI queue<int>
#define INF 1000000005
#define MAXN 100005
#define MAXSZ 1048580
#define MAXK 18
#define QPI queue<PI>
#define SWAP(x, y, T) do {T SWAP = x; x = y; y = SWAP;} while(0)
#define QPLL queue<PLL>
#define PQ priority_queue
#define UB(X, n) upper_bound(X.begin(), X.end(), n)
#define LB(X, n) lower_bound(X.begin(), X.end(), n)
#define MOD 1000000007
#define DIGS 30
#define MAXM 500
#define IT iterator
#define REV(S) reverse(S.begin(), S.end())
#define MAXN 100005
#define MAXV 1005

LL D, I, S, V, F;
vector<pair<int, string> > adj[MAXN], inadj[MAXN];
map<string, PIPI> streets;
vector<string> paths[MAXV];

int main() {
    cin >> D >> I >> S >> V >> F;

    REPZ(i, S) {
        int b, e, l; string sname;
        cin >> b >> e >> sname >> l;
        streets[sname] = MP(MP(b, e), l); 

        adj[b].PB(MP(e, sname));
        inadj[e].PB(MP(b, sname));
    }

    REPZ(i, V) {
        int p; cin >> p;
        REPZ(j, p) {
            string sname; cin >> sname;
            paths[i].PB(sname);
        }
    }

    // Naive 
    cout << I << endl;
    REPZ(i, I) {
        cout << i << endl;
        cout << inadj[i].size() << endl;
        for(auto k: inadj[i]) {
            cout << k.S << " " << 1 << endl;
        }
    }
}