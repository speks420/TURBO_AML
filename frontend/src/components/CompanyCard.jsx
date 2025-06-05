import { Box, Heading, Text, Badge, VStack, HStack, Link } from '@chakra-ui/react';
import { Link as RouterLink } from 'react-router-dom';

/**
 * CompanyCard component to display company information
 * 
 * @param {object} props - Component props
 * @param {object} props.company - Company data
 * @returns {JSX.Element} CompanyCard component
 */
const CompanyCard = ({ company }) => {
  // This is a mockup with placeholder field names
  // Actual field names would depend on the CKAN API response structure
  const {
    name = 'Company Name',
    registration_number = '12345678',
    status = 'Active',
    address = 'Company Address',
    founded_date = '2020-01-01',
  } = company || {};

  return (
    <Box
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      p={4}
      boxShadow="md"
      transition="all 0.2s"
      _hover={{ boxShadow: 'lg', transform: 'translateY(-2px)' }}
    >
      <VStack align="start" spacing={2}>
        <HStack justifyContent="space-between" w="100%">
          <Heading as="h3" size="md">
            <Link
              as={RouterLink}
              to={`/company/${registration_number}`}
              color="brand.600"
              _hover={{ textDecoration: 'underline' }}
            >
              {name}
            </Link>
          </Heading>
          <Badge colorScheme={status === 'Active' ? 'green' : 'red'}>
            {status}
          </Badge>
        </HStack>

        <Text fontSize="sm" color="gray.600">
          Registration number: {registration_number}
        </Text>

        <Text fontSize="sm">Address: {address}</Text>

        <Text fontSize="sm">Founded: {founded_date}</Text>
      </VStack>
    </Box>
  );
};

export default CompanyCard; 