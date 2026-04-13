# Quebec French Name Fuzzy Matching Implementation Plan

## 🎯 Project Overview

**Problem:** STT (Speech-to-Text) systems struggle with proper names in Quebec French, causing patient identification failures in voice agents.

**Solution:** Implement low-latency fuzzy matching using Quebec government name datasets with popularity weighting.

**Goal:** Enhance `NameSpellingAgent` to intelligently suggest correct names when STT transcription is imperfect.

---

## 📊 Available Data Sources

### Quebec Government Datasets

#### First Names (Prénoms)
- **Boys:** `banque-de-prenoms-garcons` (Retraite Québec)
  - Format: CSV with `Prenom_masculin` column
  - Data: 1980-2023 with yearly frequency counts
  - Size: ~40MB, thousands of names

- **Girls:** `banque-de-prenoms-filles` (Retraite Québec)  
  - Format: CSV with `Prenom_feminin` column
  - Data: 1980-2023 with yearly frequency counts
  - Size: ~40MB, thousands of names

#### Last Names (Noms de famille)
- **Quebec Surnames:** 5,000 most common surnames
  - Split into files: A-B, C-D, E-K, L-M, N-R, S-Z
  - Includes frequency data by region
  - Source: Institut de la statistique du Québec

#### Canadian Surnames (Future Enhancement)
- **Statistics Canada:** Comprehensive surname database
- **Access:** Through Research Data Centres (RDC)
- **Coverage:** All provinces, not just Quebec

---

## 🏗️ Architecture Overview

```
STT Input → Fuzzy Matcher → Confidence Score → Agent Decision
    ↓           ↓              ↓                 ↓
"Mare"    → ["Marie: 95%"]  → High           → Confirm "Marie"
"Jhan"    → ["Jean: 87%"]   → Medium         → Ask "Did you say Jean?"  
"Xtoph"   → ["No matches"]  → Low            → Ask for spelling
```

### Core Components

1. **NameFuzzyMatcher Service**
   - Loads Quebec name datasets
   - Performs rapid fuzzy matching
   - Returns confidence-scored suggestions

2. **Enhanced NameSpellingAgent**
   - Integrates fuzzy matching before manual spelling
   - Makes intelligent name suggestions
   - Falls back to current spelling logic

3. **Data Management System**
   - CSV loader for Quebec datasets
   - Memory-efficient name storage
   - Popularity-weighted scoring

---

## 📋 Implementation Steps

### Phase 1: Data Acquisition & Setup

#### Step 1.1: Download Quebec Datasets
```bash
# Create data directory
mkdir -p src/assets/data/names/

# Download from Quebec government:
# Boys: https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-garcons
# Girls: https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-filles
# Surnames: https://statistique.quebec.ca/fr/document/noms-de-famille-au-quebec
```

#### Step 1.2: Add Dependencies
```toml
# pyproject.toml
[tool.poetry.dependencies]
rapidfuzz = "^3.10.1"  # Fast fuzzy string matching
```

#### Step 1.3: Verify Data Structure
```csv
# Expected format for first names:
Prenom_masculin,1980,1981,...,2023,Total
ALEXANDRE,245,267,...,456,12847
JEAN,445,423,...,234,23567

# Expected format for surnames:
Nom_famille,Frequence,Region
TREMBLAY,15234,Saguenay
GAGNON,12456,Quebec
```

### Phase 2: Core Fuzzy Matching Service

#### Step 2.1: Create NameFuzzyMatcher Class
```python
# src/services/name_fuzzy_matcher.py

class NameFuzzyMatcher:
    def __init__(self):
        self.first_names_male: Dict[str, int] = {}
        self.first_names_female: Dict[str, int] = {}
        self.last_names: Dict[str, int] = {}
        
    def load_names_data(self) -> bool
    def fuzzy_match_first_name(self, input_name: str, gender: str = None) -> List[NameMatch]
    def fuzzy_match_last_name(self, input_name: str) -> List[NameMatch]
    def suggest_names(self, input_name: str, name_type: str) -> Optional[NameMatch]
```

#### Step 2.2: Implement Data Loading
- Parse Quebec CSV files
- Extract popularity data (Total column)
- Store in memory with frequency weights
- Handle special cases (TOTAL row, empty values)

#### Step 2.3: Implement Fuzzy Matching Algorithm
```python
# Fuzzy matching strategy:
1. Use rapidfuzz.fuzz.WRatio for different length tolerance
2. Apply popularity weighting (boost common names slightly)
3. Return top 5 matches with confidence scores
4. Set threshold at 70% to filter noise
```

### Phase 3: Integration with NameSpellingAgent

#### Step 3.1: Enhance Existing Functions
```python
# Add fuzzy matching before manual spelling
@function_tool
async def smart_guess_first_name(self, input_name: str, gender: str = None):
    # 1. Try fuzzy matching first
    matches = self.name_matcher.fuzzy_match_first_name(input_name, gender)
    
    # 2. If high confidence match, suggest it
    if matches and matches[0].score > 90:
        return await self.guess_first_name(...)
    
    # 3. If medium confidence, ask for confirmation
    elif matches and matches[0].score > 75:
        return await self.ask_confirmation(matches[0])
    
    # 4. If low confidence, fall back to spelling
    else:
        return await self.request_spelling()
```

#### Step 3.2: Add Smart Suggestions
```python
# New function tools for the agent
@function_tool
async def suggest_name_alternatives(self, input_name: str):
    """Present multiple name options when fuzzy matching finds several possibilities"""
    
@function_tool  
async def confirm_fuzzy_match(self, suggested_name: str, confidence: float):
    """Ask user to confirm a fuzzy-matched name"""
```

#### Step 3.3: Update Agent Prompt
```yaml
# agents/patient_identification/name_spelling.yaml
prompt: |
  You are a Quebec French name specialist agent.
  
  PRIORITY ORDER:
  1. First try fuzzy matching on the transcribed name
  2. If high confidence (>90%), suggest the match directly
  3. If medium confidence (75-90%), ask for confirmation
  4. If low confidence (<75%), ask for manual spelling
  
  Use the fuzzy matcher tools before asking users to spell names.
```

### Phase 4: Performance Optimization

#### Step 4.1: Memory Management
- Lazy loading of name datasets
- Singleton pattern for NameFuzzyMatcher
- Efficient data structures for large datasets

#### Step 4.2: Caching Strategy
```python
# Cache frequently requested matches
from functools import lru_cache

@lru_cache(maxsize=1000)
def _cached_fuzzy_match(self, input_name: str, name_type: str) -> List[NameMatch]:
```

#### Step 4.3: Benchmark Performance
- Target: <50ms response time for fuzzy matching
- Memory usage: <100MB for all name datasets
- Test with 1000+ name variations

### Phase 5: Advanced Features

#### Step 5.1: Context-Aware Matching
```python
# Consider conversation context
def fuzzy_match_with_context(self, input_name: str, conversation_history: List[str]):
    # If previous names were French, boost French names
    # If patient mentioned gender, use appropriate dataset
```

#### Step 5.2: Phonetic Matching
```python
# Add phonetic algorithms for Quebec French
from metaphone import doublemetaphone

def phonetic_match(self, input_name: str):
    # Handle Quebec French specific phonetic patterns
    # "Jean" vs "Jeanne" pronunciation differences
```

#### Step 5.3: Regional Preferences
```python
# Use Quebec regional data for surname preferences
def regional_surname_boost(self, surname: str, region: str):
    # Boost "Tremblay" in Saguenay region
    # Boost "Roy" in Montreal region
```

---

## 🔧 Technical Considerations

### Data Management

#### CSV Processing
```python
# Handle Quebec-specific CSV formatting:
- UTF-8 encoding for accented characters (É, È, À)
- Comma vs semicolon delimiters  
- Windows vs Unix line endings
- "TOTAL" summary row exclusion
```

#### Memory Efficiency
```python
# Optimize for large datasets:
- Use sets for exact matching pre-filter
- Store names in uppercase for consistency
- Use integer frequencies vs float percentages
- Implement incremental loading for huge files
```

### Fuzzy Matching Tuning

#### Score Calibration
```python
# Confidence thresholds for Quebec French:
EXACT_MATCH = 95      # "Marie" -> "MARIE" 
HIGH_CONFIDENCE = 85  # "Marie" -> "MARI"
MEDIUM_CONFIDENCE = 75 # "Mare" -> "MARIE" 
LOW_CONFIDENCE = 60   # "Mar" -> "MARIE"
REJECT_THRESHOLD = 50 # Below this, don't suggest
```

#### Algorithm Selection
```python
# RapidFuzz scorer comparison:
- fuzz.ratio: Basic Levenshtein distance
- fuzz.partial_ratio: Good for partial matches
- fuzz.token_sort_ratio: Word order independent  
- fuzz.WRatio: Weighted combination (RECOMMENDED)
```

### Error Handling

#### Graceful Degradation
```python
# If fuzzy matcher fails:
1. Log error but continue with original flow
2. Fall back to manual spelling immediately
3. Don't crash the agent session
4. Provide user feedback: "Let me ask you to spell that"
```

#### Data Validation
```python
# Validate CSV data quality:
- Check for required columns
- Verify numeric frequency values
- Handle missing/corrupted entries
- Warn about dataset age (>2 years old)
```

---

## 🧪 Testing Strategy

### Unit Tests

#### NameFuzzyMatcher Tests
```python
def test_fuzzy_match_first_name():
    # Test exact matches
    assert matcher.fuzzy_match_first_name("MARIE")[0].score > 95
    
    # Test common STT errors
    assert "MARIE" in [m.name for m in matcher.fuzzy_match_first_name("Mare")]
    
    # Test gender filtering  
    male_matches = matcher.fuzzy_match_first_name("Jean", gender="male")
    assert all("JEAN" in m.name for m in male_matches)
```

#### Integration Tests
```python
def test_name_spelling_agent_integration():
    # Test agent uses fuzzy matching before spelling
    # Test confidence thresholds trigger correct responses
    # Test fallback to manual spelling works
```

### Performance Tests

#### Benchmark Suite
```python
def benchmark_fuzzy_matching():
    # Test 1000 random names
    # Measure response time (target: <50ms)
    # Measure memory usage (target: <100MB)
    # Test concurrent requests
```

### User Acceptance Testing

#### Quebec French Speakers
```python
# Test with real Quebec French speakers:
- Test common STT errors they experience
- Validate name suggestions feel natural
- Test regional name variations
- Verify pronunciation handling
```

---

## 📈 Success Metrics

### Performance KPIs
- **Response Time:** <50ms for fuzzy matching
- **Memory Usage:** <100MB for full dataset
- **Accuracy:** >90% correct suggestions for common names
- **Coverage:** Handle >95% of Quebec first names

### User Experience KPIs  
- **Reduced Spelling Requests:** 60% fewer manual spelling sessions
- **Faster Name Resolution:** 30% faster patient identification
- **User Satisfaction:** Reduced frustration with name entry

### Technical KPIs
- **System Reliability:** 99.9% uptime for fuzzy matching service
- **Error Rate:** <1% fuzzy matching failures
- **Data Freshness:** Annual updates of Quebec name datasets

---

## 🚀 Deployment Plan

### Development Environment
1. Set up local Quebec datasets
2. Implement and test fuzzy matching service
3. Unit test all components
4. Integration test with NameSpellingAgent

### Staging Environment  
1. Deploy with sample Quebec datasets
2. Performance testing with load simulation
3. User acceptance testing with Quebec French speakers
4. Monitor memory usage and response times

### Production Rollout
1. **Phase 1:** Deploy to 10% of traffic (A/B test)
2. **Phase 2:** Monitor success metrics for 1 week
3. **Phase 3:** Full rollout if metrics meet targets
4. **Phase 4:** Monitor and optimize based on real usage

### Monitoring & Maintenance
```python
# Key metrics to monitor:
- Fuzzy matching response times
- Memory usage of name datasets  
- Cache hit rates
- User spelling session reduction
- Error rates and fallback frequency
```

---

## 🔮 Future Enhancements

### Phase 2: Canadian Coverage
- Integrate Statistics Canada surname data
- Add English Canadian first names
- Support bilingual name variations

### Phase 3: Machine Learning
- Train custom models on Quebec French STT errors
- Implement neural fuzzy matching
- Learn from user corrections

### Phase 4: Real-time Updates
- Connect to live Quebec birth registry
- Auto-update popular name trends
- Regional preference learning

---

## 📚 Resources & References

### Quebec Government Data Sources
- [Banque de prénoms - Garçons](https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-garcons)
- [Banque de prénoms - Filles](https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-filles)  
- [Noms de famille au Québec](https://statistique.quebec.ca/fr/document/noms-de-famille-au-quebec)

### Statistics Canada Resources
- [Research Data Centres Program](https://www.statcan.gc.ca/en/microdata/data-centres)
- [Record Linkage Guidelines](https://www.statcan.gc.ca/en/record-linkage)

### Technical Libraries
- [RapidFuzz Documentation](https://maxbachmann.github.io/RapidFuzz/)
- [Quebec French Phonetics Research](https://www.erudit.org/en/journals/meta/)

### Implementation References
- LiveKit Agent Framework Documentation
- Pydantic Data Validation Patterns
- CSV Processing Best Practices for Quebec Data

---

## ✅ Action Items

### Immediate (Week 1)
- [ ] Download Quebec first names datasets (boys & girls)
- [ ] Download Quebec surnames datasets (6 files)
- [ ] Verify data quality and structure
- [ ] Set up development environment

### Short Term (Week 2-3)
- [ ] Implement NameFuzzyMatcher service
- [ ] Add rapidfuzz dependency
- [ ] Write unit tests for fuzzy matching
- [ ] Create sample integration with NameSpellingAgent

### Medium Term (Week 4-6)
- [ ] Full integration with NameSpellingAgent
- [ ] Performance optimization and caching
- [ ] User acceptance testing
- [ ] Documentation and deployment guides

### Long Term (Month 2+)
- [ ] Production deployment with monitoring
- [ ] Statistics Canada surname integration
- [ ] Machine learning enhancements
- [ ] Regional preference features

---

*This implementation plan provides a comprehensive roadmap for solving STT limitations in Quebec French voice agents through intelligent fuzzy name matching.* 