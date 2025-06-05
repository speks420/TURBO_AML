import { useState } from 'react';
import { 
  Input, 
  InputGroup, 
  InputRightElement, 
  IconButton, 
  Box 
} from '@chakra-ui/react';

/**
 * SearchBar component for searching companies
 * 
 * @param {object} props - Component props
 * @param {function} props.onSearch - Function called when search is triggered
 * @returns {JSX.Element} SearchBar component
 */
const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query);
    }
  };

  return (
    <Box as="form" onSubmit={handleSearch} w="100%">
      <InputGroup size="lg">
        <Input
          placeholder="Search for companies by name, registration number..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          borderRadius="md"
          boxShadow="sm"
        />
        <InputRightElement>
          <IconButton
            aria-label="Search"
            icon={<span>🔍</span>}
            type="submit"
            h="1.75rem"
            size="sm"
            variant="ghost"
          />
        </InputRightElement>
      </InputGroup>
    </Box>
  );
};

export default SearchBar; 