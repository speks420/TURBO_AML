import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  VStack,
  Heading,
  Text,
  SimpleGrid,
  Alert,
  AlertIcon,
  Box,
  Button,
  HStack,
  Center,
  useDisclosure
} from '@chakra-ui/react';
import { TimeIcon } from '@chakra-ui/icons';
import Layout from '../components/layout/Layout';
import SearchBar from '../components/ui/SearchBar';
import CompanyCard from '../components/ui/CompanyCard';
import LoadingSpinner from '../components/ui/LoadingSpinner';
import SearchHistoryDrawer from '../components/ui/SearchHistoryDrawer';
import useSearch from '../hooks/useSearch';

/**
 * HomePage component
 * 
 * @returns {JSX.Element} HomePage component
 */
const HomePage = () => {
  const navigate = useNavigate();
  const {
    isLoading,
    error,
    results,
    search,
    nextPage,
    previousPage,
    hasNextPage,
    hasPreviousPage,
    page
  } = useSearch();
  const [hasSearched, setHasSearched] = useState(false);
  const { isOpen, onOpen, onClose } = useDisclosure();

  const handleSearch = (query) => {
    search(query);
    setHasSearched(true);
  };
  
  const handleCompanySelect = (regNumber) => {
    navigate(`/company/${regNumber}`);
  };

  return (
    <Layout>
      <VStack spacing={8} align="stretch">
        <Box textAlign="center" my={10}>
          <Heading as="h1" size="2xl" mb={4} color="brand.600">
            TURBO_AML
          </Heading>
          <Text fontSize="xl" color="gray.600">
            Search for Latvian companies by name, registration number, etc.
          </Text>
        </Box>

        <Box mb={6}>
          <HStack spacing={4} align="flex-start">
            <Box flex="1">
              <SearchBar onSearch={handleSearch} />
            </Box>
            <Button 
              rightIcon={<TimeIcon />} 
              colorScheme="brand" 
              variant="outline" 
              size="md"
              onClick={onOpen}
              flexShrink={0}
            >
              Recent
            </Button>
          </HStack>
        </Box>

        <SearchHistoryDrawer 
          isOpen={isOpen} 
          onClose={onClose} 
          onCompanySelect={handleCompanySelect} 
        />

        {isLoading && <LoadingSpinner text="Searching companies..." />}

        {error && (
          <Alert status="error">
            <AlertIcon />
            {error}
          </Alert>
        )}

        {!isLoading && !error && hasSearched && results.companies.length === 0 && (
          <Center py={10}>
            <Text>No companies found. Try a different search term.</Text>
          </Center>
        )}

        {!isLoading && !error && results.companies.length > 0 && (
          <Box>
            <Text mb={4}>
              Found {results.count} {results.count === 1 ? 'company' : 'companies'}
            </Text>

            <SimpleGrid columns={{ base: 1, md: 2 }} spacing={6}>
              {results.companies.map((company) => (
                <CompanyCard key={company.registration_number} company={company} />
              ))}
            </SimpleGrid>

            {(hasNextPage || hasPreviousPage) && (
              <HStack justify="center" mt={8} spacing={4}>
                <Button
                  onClick={previousPage}
                  isDisabled={!hasPreviousPage}
                  colorScheme="gray"
                >
                  Previous
                </Button>
                <Text>
                  Page {page + 1} of {Math.ceil(results.count / 10)}
                </Text>
                <Button onClick={nextPage} isDisabled={!hasNextPage} colorScheme="brand">
                  Next
                </Button>
              </HStack>
            )}
          </Box>
        )}
      </VStack>
    </Layout>
  );
};

export default HomePage; 